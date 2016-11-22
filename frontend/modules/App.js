import React from 'react'

export default React.createClass({
    getInitialState: function () {
        return {parcelId: ''};
    },

    handleParcelIdChange: function (e) {
        this.setState({parcelId: e.target.value});
    },
    handleSubmit: function (e) {
        e.preventDefault();
        var parcelId = this.state.parcelId.trim().toUpperCase();
        if (!parcelId) {
            return;
        }
        // Todo: Redirect
    },

    render() {
        return <div className="page-content-wrapper text-09">
            <div className="container-fluid">
                <div className="row title-row">
                    <div className="col-xs-12">
                        <div className="pull-sm-left store-home"><a href=""
                                                                    className="store-home--text">Track order
                            status</a>
                            <form className="tracking-widget -responsive">
                                <div className="tracking-widget-ui">
                                    <input type="text" className="text-large text-input"
                                           placeholder="Tracking Number" value={this.state.parcelId}
                                           onChange={this.handleParcelIdChange}/>
                                    <button value="submit" type="submit" className="btn">
                                        <span className="btn__text">Track</span>
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    }
})
